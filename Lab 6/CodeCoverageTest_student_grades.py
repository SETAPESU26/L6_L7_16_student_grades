import pytest

from student_grades import exam_eligibility, final_marks, letter_grade


@pytest.mark.parametrize(
    ("marks", "expected"),
    [
        (95, "S"),
        (85, "A"),
        (75, "B"),
        (65, "C"),
        (55, "D"),
        (45, "E"),
        (39, "F"),
    ],
)
def test_letter_grade_returns_each_grade(marks, expected):
    assert letter_grade(marks) == expected


def test_letter_grade_rejects_negative_marks():
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(-1)


def test_final_marks_rejects_internal_marks_over_limit():
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(41, 0, True)


def test_final_marks_caps_project_bonus_at_100():
    assert final_marks(40, 60, True) == 100


def test_exam_eligibility_blocks_unpaid_fees():
    assert exam_eligibility(100, False, True) == "blocked"


def test_exam_eligibility_allows_attendance_with_medical_reason():
    assert exam_eligibility(70, True, True) == "eligible"


def test_exam_eligibility_meets_attendance_requirement():
    assert exam_eligibility(75, True, False) == "eligible"


def test_exam_eligibility_detains_low_attendance():
    assert exam_eligibility(64, True, False) == "detained"