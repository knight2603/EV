from app.memory.database import get_connection


class MemoryManager:

    def save_memory(
        self,
        content: str,
        category: str = "general",
        importance: int = 1
    ):
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            INSERT INTO memories
            (content, category, importance)
            VALUES (?, ?, ?)
            """,
            (content, category, importance)
        )

        connection.commit()
        connection.close()

    def get_memories(self):

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT id, content, category, importance
            FROM memories
            ORDER BY importance DESC, created_at DESC
            """
        )

        memories = cursor.fetchall()

        connection.close()

        return memories
    
    def search_memories(self, query: str):
        
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute(
            """
            SELECT id, content, category, importance
            FROM memories
            WHERE content LIKE ?
            ORDER BY importance DESC, created_at DESC
            """,
            (f"%{query}%",)
        )
        
        memories = cursor.fetchall()
        
        connection.close()
        
        return memories