from pathlib import Path
import pytest
import pandas as pd
import taxi_rides_outlier_detection.outlier_detector as outlier_detector

# SELECT * FROM data WHERE STRFTIME('%Y-%m-%d', tpep_pickup_datetime) = '2025-01-15'

#import pandas as pd
#df = pd.read_parquet("data/taxi_ride_data.parquet")
#daily_data =  df[df['tpep_pickup_datetime'].dt.date == pd.to_datetime('2025-01-15').date()]
#test_data = daily_data.sample(frac=0.2, random_state=42).reset_index(drop=True)
#test_data.to_parquet("tests/taxi_rides_outlier_detection/taxi_ride_test_data.parquet")

@pytest.fixture
def taxi_rides_test_data() -> pd.DataFrame: 
    from pathlib import Path
    module_dir = Path(__file__).parent
    return pd.read_parquet(module_dir / "taxi_ride_test_data.parquet") 

def test_detect_outliers(taxi_rides_test_data): 
    outliers, metadata = outlier_detector.detect_outliers(taxi_rides_test_data)
    assert len(outliers) == 20
    assert outliers.columns.tolist() == ['ride_dist', 'ride_time', 'date', 'ride_id']