import pytest
import graphics.instance_step_rate as mod

CASES = [
    ("divisor_by_attribute", (1,)),
    ("bind_after_upload", (1,)),
    ("length_same_frame", (1,)),
    ("rebuild_on_material", (1,)),
    ("skip_empty", (1,)),
    ("validate_step", (1,)),
    ("load", (1,)),
    ("upload", (1,)),
    ("cull", (1,)),
    ("draw", (1,)),
    ("bind", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
