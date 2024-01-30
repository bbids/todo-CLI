## Priority Levels
    - Priority 0: Critical
    - Priority 1: Important
    - Priority 2: Necessary
    - Priority 3: Non-urgent
    - Priority 4: Optional

    Other priorities have no default meaning assosiated with them.

## Task format
    sample_task = {
        "ID": id,
        "Priority": priority,
        "Content": content,
        "DueDate": None,
        "Category": None,
    }

## Config.json
    To be accessable via config command in the future.

## Create
    - automatically sets the current To-Do in config file to the new To-Do