<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class NewsController extends Controller
{
    public function index()
    {
        return view('news');
    }
    public function analyze(Request $request)
    {
        $text = $request->input('text');
        $response = Http::post('http://127.0.0.1:5000/predict', ['text' => $text]);
        // dd($response);
        if ($response->successful()) {
            // Mendapatkan data JSON dari badan respons
            $responseData = $response->json();

            // Mendapatkan prediksi sentiment dari data JSON
            $predict = $responseData['predict'];
            // dd($predict);
            // Mengembalikan view 'form' dengan data prediksi
            return view('news')->with('predict', $predict);
        } else {
            // Mengembalikan view 'form' dengan pesan kesalahan jika respons tidak sukses
            return view('news')->with('error', 'Error: ' . $response->status());
        }
        // return view('news')->with('prediction', $prediction);
        
        
    }
}
