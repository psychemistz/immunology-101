"""Optional Claude AI integration for adaptive explanations."""

from __future__ import annotations

from immunology101.prompts import TUTOR_SYSTEM_PROMPT, build_exercise_context

AI_MODEL = "claude-sonnet-4-6"


def is_available() -> bool:
    """Check if the anthropic package and API key are available."""
    try:
        import anthropic
        return bool(anthropic.Anthropic().api_key)
    except Exception:
        return False


def ask_tutor(
    lesson_title: str,
    lesson_excerpt: str,
    exercise_question: str,
    exercise_explanation: str,
    student_question: str,
) -> str | None:
    """Ask the AI tutor a follow-up question about an exercise.

    Returns the AI response, or None if AI is not available.
    """
    try:
        import anthropic
    except ImportError:
        return None

    try:
        client = anthropic.Anthropic()
        user_message = build_exercise_context(
            lesson_title=lesson_title,
            lesson_excerpt=lesson_excerpt,
            exercise_question=exercise_question,
            exercise_explanation=exercise_explanation,
            student_question=student_question,
        )
        response = client.messages.create(
            model=AI_MODEL,
            max_tokens=1024,
            system=TUTOR_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.content[0].text
    except Exception:
        return None
