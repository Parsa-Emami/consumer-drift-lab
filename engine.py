def evaluate(data, fixture_path):
    removed = set(data["removed_operations"])
    covered = set()
    findings = []
    for consumer, operations in sorted(data["consumers"].items()):
        covered.update(operations)
        for operation in sorted(removed.intersection(operations)):
            findings.append({"code": "consumer_affected", "consumer": consumer, "operation": operation})
    for operation in sorted(removed - covered):
        findings.append({"code": "removed_operation_without_contract", "operation": operation})
    return findings
