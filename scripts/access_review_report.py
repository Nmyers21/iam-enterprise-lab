sample_review_data = [
    {"user": "David Patel", "issue": "Retained CRM access after department change", "action": "Removed access"},
    {"user": "Kevin Reed", "issue": "Inactive contractor account", "action": "Disabled account"},
    {"user": "Michael Torres", "issue": "Privileged access review completed", "action": "No change required"}
]

def generate_access_review_report(review_data):
    print("=== Quarterly Access Review Report ===")
    print(f"Total Records Reviewed: {len(review_data)}")
    print()

    for entry in review_data:
        print(f"User: {entry['user']}")
        print(f"Issue: {entry['issue']}")
        print(f"Action: {entry['action']}")
        print("-" * 40)

if __name__ == "__main__":
    generate_access_review_report(sample_review_data)