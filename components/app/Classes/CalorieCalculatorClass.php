<?php 

namespace App\Classes;
use Carbon\Carbon;

class CalorieCalculatorClass {

	public function get_data( $age, $gender, $unit, $height_metric, $weight_metric, $height_us_feet, $height_us_inch, $weight_us, $level )
	{

        try {

            // Initialize data array
            $data = [];

            // Calculate TDEE based on unit
            if ($unit == 'metric') {
                // Metric calculations
                $calorie = ($gender == 'female') ? (10 * $weight_metric + 6.25 * $height_metric - 5 * $age - 161) : (10 * $weight_metric + 6.25 * $height_metric - 5 * $age + 5);
            } else {
                // US unit calculations
                $feetToInch = $height_us_feet * 12 + intval($height_us_inch);
                $calorie       = ($gender == 'female') ? (10 * $weight_us + 6.25 * $feetToInch - 5 * $age - 161) : (10 * $weight_us + 6.25 * $feetToInch - 5 * $age + 5);
            }

            // Multiply by activity level and round
            $data['calorie'] = round($calorie * $level);

            return $data;
            
        } catch (\Exception $e) {

            session()->flash('status', 'error');
            session()->flash('message', __($e->getMessage()));
            return;
        }

	}

}