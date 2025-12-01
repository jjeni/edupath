import sqlite3
import time
import logging
from typing import List, Dict, Any

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(name)s | %(levelname)s | %(message)s')
logger = logging.getLogger("EduPath.Core")

class SQLiteMemoryBank:
    """
    Persistent Storage Layer (Singleton Pattern).
    Stores student history and class-wide analytics.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SQLiteMemoryBank, cls).__new__(cls)
            cls._instance._initialize_db()
        return cls._instance

    def _initialize_db(self):
        self.conn = sqlite3.connect("edupath_enterprise.db", check_same_thread=False)
        cursor = self.conn.cursor()
        
        # Table 1: Weaknesses (For Class Trends)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS weaknesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_name TEXT,
                topic TEXT,
                severity TEXT,
                timestamp REAL
            )
        ''')
        self.conn.commit()
        logger.info("✅ Database Initialized")

    def log_weakness(self, student: str, topic: str, severity: str):
        cursor = self.conn.cursor()
        cursor.execute('INSERT INTO weaknesses (student_name, topic, severity, timestamp) VALUES (?, ?, ?, ?)',
                       (student, topic.lower().strip(), severity, time.time()))
        self.conn.commit()
        logger.info(f"📉 [DB] Logged weakness: {student} -> {topic}")

    def get_student_history(self, student: str) -> str:
        cursor = self.conn.cursor()
        cursor.execute('SELECT topic, severity, timestamp FROM weaknesses WHERE student_name = ?', (student,))
        rows = cursor.fetchall()
        if not rows:
            return f"No records found for {student}."
        return "\n".join([f"- {row[0]} ({row[1]})" for row in rows])

    def check_class_trends(self, threshold=2) -> str:
        """Finds topics where multiple students are failing."""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT topic, COUNT(DISTINCT student_name) as count 
            FROM weaknesses 
            GROUP BY topic 
            HAVING count >= ?
        ''', (threshold,))
        rows = cursor.fetchall()
        if rows:
            alerts = [f"TOPIC: '{r[0]}' (Failing Students: {r[1]})" for r in rows]
            return f"🚨 CLASS RESCHEDULE ALERT! High failure rate detected in:\n" + "\n".join(alerts)
        return "✅ Class performance nominal."

# Global Instance
db = SQLiteMemoryBank()