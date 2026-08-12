from app.core.session_manager import SessionManager


session1 = SessionManager()
session2 = SessionManager()


print("=== SESSION 1 ===")
print(session1.get_session_id())

print("\n=== SESSION 2 ===")
print(session2.get_session_id())


print("\n¿Son diferentes?")

print(
    session1.get_session_id()
    != session2.get_session_id()
)