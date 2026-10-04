<?php 

namespace App\Classes;
use Carbon\Carbon;

class HoursCalculatorClass {

	public function get_data( $startTime, $endTime )
	{

        try {

            $duration              = Carbon::parse($startTime)->diff($endTime);

            $data['hours']         = $duration->format('%H');

            $data['minutes']       = $duration->format('%I');

            $data['total_minutes'] = Carbon::parse($startTime)->diffInMinutes($endTime);

            return $data;
            
        } catch (\Exception $e) {

            session()->flash('status', 'error');
            session()->flash('message', __($e->getMessage()));
            return;
        }

	}

}