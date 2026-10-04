<?php

namespace App\Http\Livewire\Public\Install;

use Livewire\Component;
use App\Models\Admin\User;
use DateTime;
use Brotzka\DotenvEditor\DotenvEditor;
use App\Models\Install;

class Account extends Component
{
    public $email;
    public $password;

    public function mount(){
        $install                  = Install::findOrFail(1);
        if ($install->database    == false) return redirect()->route('sw_database');
    }

    public function render()
    {
        return view('livewire.public.install.account')->layout('layouts.install');
    }

    /**
     * -------------------------------------------------------------------------------
     *  onCreateAdminAccount
     * -------------------------------------------------------------------------------
    **/
    public function onCreateAdminAccount(){

        $this->validate([
            'email'    => 'required|email',
            'password' => 'required'
        ]);

        if ( User::find(1) === null ) {

            $user                    = new User;
            $user->id                = 1;
            $user->fullname          = 'Admin';
            $user->position          = 'Administrator';
            $user->address           = '121 King Street, Melbourne Victoria 3000, Australia';
            $user->phone             = '+61 3 8376 6284';
            $user->email             = $this->email;
            $user->password          = bcrypt($this->password);
            $user->bio               = 'Administrator';
            $user->gender            = 1;
            $user->avatar            = asset('assets/img/avatar.jpg');
            $user->social_status     = true;
            $user->is_admin          = true;
            $user->email_verified_at = new DateTime();
            $user->created_at        = new DateTime();
            $user->save();

            $install          = Install::findOrFail(1);
            $install->account = true;
            $install->save();

            return redirect()->route('sw_import');

        }
        else {

            $user             = User::findOrFail(1);
            $user->email      = $this->email;
            $user->password   = bcrypt($this->password);
            $user->is_admin   = true;
            $user->email_verified_at = new DateTime();
            $user->updated_at = new DateTime();
            $user->save();

            $install          = Install::findOrFail(1);
            $install->account = true;
            $install->save();

            return redirect()->route('sw_import');
        }

    }
}
