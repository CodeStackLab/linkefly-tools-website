<?php 

namespace App\Classes;
use Carbon\Carbon;

class DaysCalculatorClass {

	public function get_data( $startDate, $endDate )
	{

        try {

            $data['days'] = Carbon::parse($startDate)->diffInDays($endDate);

            return $data;
            
        } catch (\Exception $e) {

            session()->flash('status', 'error');
            session()->flash('message', __($e->getMessage()));
            return;
        }

	}

}