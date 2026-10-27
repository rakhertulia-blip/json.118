STATUSES = ["pending", "pass", "fail"]
def valid_cases(data):
        if type(data) is not list:
            return False

        ids = []

        for item in data:
            if type(item) is not dict:
                return False

            if (item.keys()) != {"id", "title", "status"}:
                return False

            case_id = item["id"]
            title = item["title"]
            status = item["status"]

            if type(case_id) is not int or case_id <= 0:
                return False

            if case_id in ids:
                return False

            ids.append(case_id)

            if type(title) is not str or len(title.strip()) < 5:
                return False

            if type(status) is not str or status not in STATUSES:
                return False

        return True

def add_case(items, title):
        if type(title) is not str:
            return None

        title = title.strip()

        if len(title) < 5:
            return None

        max_id = 0

        for item in items:
            if item["id"] > max_id:
                max_id = item["id"]

        new_id = max_id + 1

        items.append({"id": new_id,"title": title,"status": "pending"})

        return new_id

def set_result(items, case_id, status):
        if type(status) is not str:
            return "invalid_status"

        status = status.strip().lower()

        if status not in STATUSES:
            return "invalid_status"

        for item in items:
            if item["id"] == case_id:
                if item["status"] == status:
                    return "unchanged"

                item["status"] = status
                return "updated"

        return "not_found"

def summarize(items):
        result = {"total": len(items),"pending": 0,"pass": 0,"fail": 0 }

        for item in items:
            result[item["status"]] += 1

        return result