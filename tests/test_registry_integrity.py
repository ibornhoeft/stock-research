from metrics.registry import METRIC_REGISTRY


def test_registry_non_empty():
    assert len(METRIC_REGISTRY) > 0


def test_registry_unique_names():
    names = [spec.name for spec in METRIC_REGISTRY.values()]
    assert len(names) == len(set(names))


def test_registry_has_required_fields():
    for spec in METRIC_REGISTRY.values():
        assert spec.name
        assert callable(spec.function)
        assert isinstance(spec.inputs, list)
        assert isinstance(spec.parameters, list)
        assert spec.family