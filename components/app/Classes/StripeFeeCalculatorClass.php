<?php 

namespace App\Classes;
use Carbon\Carbon;

class StripeFeeCalculatorClass {

    public function get_data($amount)
    {
        try {
            // Calculate the Stripe fee
            $fee = $this->calculateStripeFee($amount);

            // Calculate the required charge amount to receive the specified net amount
            $chargeAmount = $this->calculateRequiredChargeAmount($amount);

            // Prepare the data to return
            $data = [
                'original_amount' => $amount,
                'stripe_fee'      => round($fee, 2),
                'net_amount'      => round($amount - $fee, 2),
                'charge_amount'   => round($chargeAmount, 2)
            ];

            return $data;

        } catch (\Exception $e) {
            session()->flash('status', 'error');
            session()->flash('message', __($e->getMessage()));
            return;
        }
    }

    /**
     * -------------------------------------------------------------------------------
     *  calculateStripeFee
     * -------------------------------------------------------------------------------
    **/
    public function calculateStripeFee($amount)
    {
        // Define Stripe's fee structure
        $percentageFee = 0.029; // 2.9% per transaction (as an example, this varies)
        $fixedFee = 0.30;       // 30 cents per transaction (as an example, this varies)

        // Calculate the fee
        $stripeFee = ($amount * $percentageFee) + $fixedFee;

        // Return the fee
        return $stripeFee;
    }

    /**
     * -------------------------------------------------------------------------------
     *  calculateRequiredChargeAmount
     * -------------------------------------------------------------------------------
    **/
    public function calculateRequiredChargeAmount($desiredNetAmount)
    {
        $percentageFee = 0.029; // 2.9% per transaction
        $fixedFee = 0.30;       // 30 cents per transaction
        $chargeAmount = $desiredNetAmount;
        $increment = 0.01; // Increment to adjust charge amount

        while (true) {
            $fee = ($chargeAmount * $percentageFee) + $fixedFee;
            $netAmount = $chargeAmount - $fee;

            if ($netAmount >= $desiredNetAmount) {
                break;
            }

            $chargeAmount += $increment;
        }

        return round($chargeAmount, 2); // Rounding to 2 decimal places
    }

}