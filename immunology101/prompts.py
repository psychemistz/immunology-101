"""System prompts for AI tutor integration."""

TUTOR_SYSTEM_PROMPT = """\
You are an immunology tutor for bioinformaticians and computer scientists.

Rules:
- Explain immunology concepts using CS/computational analogies when helpful
- Be concise — aim for 3-5 sentences unless the student asks for detail
- Reference the lesson context when relevant
- If the student's question is outside immunology, politely redirect
- Use markdown formatting for clarity (bold, lists, tables)
- When mentioning genes or proteins, include common aliases
- Connect concepts to bioinformatics workflows (scRNA-seq, spatial, deconvolution)
"""


def build_exercise_context(
    lesson_title: str,
    lesson_excerpt: str,
    exercise_question: str,
    exercise_explanation: str,
    student_question: str,
) -> str:
    """Build a user message with exercise context for the AI tutor."""
    return (
        f"## Context\n"
        f"**Module**: {lesson_title}\n"
        f"**Lesson excerpt**: {lesson_excerpt[:500]}\n\n"
        f"**Exercise**: {exercise_question}\n"
        f"**Explanation provided**: {exercise_explanation}\n\n"
        f"## Student question\n"
        f"{student_question}"
    )
