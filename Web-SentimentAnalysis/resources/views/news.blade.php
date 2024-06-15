<!DOCTYPE html>
<html>
<head>
    <title>Sentiment Analysis</title>
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            padding: 0;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        textarea {
            width: 100%;
            height: 100px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            resize: none;
            font-size: 14px;
        }
        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 10px;
            display: block;
            width: 100%;
        }
        button:hover {
            background-color: #0056b3;
        }
        #result {
            margin-top: 20px;
            font-size: 18px;
            text-align: center;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            background: #f9f9f9;
        }
        #result2 {
            margin-top: 20px;
            font-size: 18px;
            text-align: center;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            background: #red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Sentiment Analysis</h1>
        <form action="{{ route('analyze') }}" method="POST">
            @csrf
            <textarea name="text" rows="5" cols="50"></textarea>
            <button type="submit">Analyze</button>
        </form>
        @isset($predict)
        <div id="result">
            Prediction: {{ $predict }}
        </div>
    @endisset

    <!-- Bagian untuk menampilkan pesan kesalahan -->
    @isset($error)
        <div id="result2">
            Error: {{ $error }}
        </div>
    @endisset
    </div>
    
</body>
</html>
