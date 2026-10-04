<?php 

namespace App\Classes;
use Carbon\Carbon;

class MonthCalculatorClass {

	public function get_data( $startDate, $endDate )
	{

        try {

            $diff = Carbon::parse($startDate)->diff($endDate);

            $data['months'] = $diff->m; // Number of months
            $data['days'] = $diff->d;   // Number of days

            return $data;
            
        } catch (\Exception $e) {

            session()->flash('status', 'error');
            session()->flash('message', __($e->getMessage()));
            return;
        }

	}

}