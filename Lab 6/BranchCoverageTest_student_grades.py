import pytest

from student_grades import exam_eligibility, final_marks, letter_grade


@pytest.mark.parametrize(
    ("marks", "expected"),
    [
        (0, "F"),
        (39, "F"),
        (40, "E"),
        (49, "E"),
        (50, "D"),
        (59, "D"),
        (60, "C"),
        (69, "C"),
        (70, "B"),
        (79, "B"),
        (80, "A"),
        (89, "A"),
        (90, "S"),
        (100, "S"),
    ],
)
def test_letter_grade_boundaries(marks, expected):
    assert letter_grade(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_letter_grade_rejects_marks_outside_range(marks):
    with pytest.raises(ValueError, match="invalid marks"):
        letter_grade(marks)


@pytest.mark.parametrize(
    ("internal", "external"),
    [(41, 0), (0, 61)],
)
def test_final_marks_rejects_each_component_over_limit(internal, external):
    with pytest.raises(ValueError, match="marks out of range"):
        final_marks(internal, external, False)


def test_final_marks_without_project():
    assert final_marks(30, 50, False) == 80


def test_final_marks_project_bonus_below_cap():
    assert final_marks(20, 30, True) == 55


def test_final_marks_project_bonus_is_capped():
    assert final_marks(40, 60, True) == 100


def test_exam_eligibility_blocks_when_fees_are_unpaid():
    assert exam_eligibility(100, False, True) == "blocked"


def test_exam_eligibility_meets_attendance_requirement():
    assert exam_eligibility(75, True, False) == "eligible"


def test_exam_eligibility_medical_exception_at_threshold():
    assert exam_eligibility(65, True, True) == "eligible"


@pytest.mark.parametrize(
    ("attendance", "has_medical"),
    [(65, False), (64, True)],
)
def test_exam_eligibility_detains_when_exception_does_not_apply(
    attendance, has_medical
):
    assert exam_eligibility(attendance, True, has_medical) == "detained"