from datetime import datetime, timezone
from fastapi import HTTPException

def process_classification(raw_data:dict)->dict:
    """
    """
    gender = raw_data.get("gender")
    count = raw_data.get("count", 0)

    # EDGE CASES
    # ---------------------
    # No gender or 0 count
    if gender is None or count == 0:
        raise HTTPException(
            status_code=422,
            detail="No prediction available for the provided name"
        )
    
    # LOGIC
    probability = raw_data.get("probability", 0.0)
    is_confident = (probability >= 0.7) and (count >= 100)


    # Data Transformation and timestamps
    return{
        "name": raw_data.get("name"),
        "gender" : gender,
        "probability" : probability,
        "sample_size" : count,
        "is_confident" : is_confident,
        "processed_at": datetime.now(timezone.utc)
    }