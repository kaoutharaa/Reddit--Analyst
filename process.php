<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reddit Analysis Results</title>
    <style>
        body {
            font-family: sans-serif;
            background-color: #1E293B;  
            color: #CBD5E1;  
            margin: 0;
            padding: 20px;
        }
        h2 {
            color: #F9806F;  
            margin-top: 20px;
            margin-bottom: 10px;
            text-align: center;
        }
        pre {
            background-color: #334155;  
            color: #E2E8F0;
            padding: 15px;
            border-radius: 5px;
            overflow: auto;  
            max-height: 300px;
            white-space: pre-wrap; 
        }
        p {
            color: #FCA5A5;  
            background-color: #7F1D1D;
            border: 1px solid #FDA7A7;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
            text-align: center;
        }
        img {
            max-width: 80%;
            height: auto;
            display: block;
            margin: 20px auto;  
            border-radius: 5px;  
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);  
        }
        .container {
            max-width: 960px;
            margin: 0 auto; 
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="container">
        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $subreddit = $_POST['analyzed_subreddits'];
            $comments_per_post = $_POST['comments-per-post'];
 
            $python = "C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python312\\python.exe";
            $script = "C:\\xampp\\folder\\htdocs\\application_web\\projet_python\\script.py";

            
            $command = "$python " . escapeshellarg($script) . " " . escapeshellarg($subreddit) . " " . escapeshellarg($comments_per_post);
 
            $output = shell_exec($command . " 2>&1");
 
            $lines = explode("\n", $output);
            $image_path = '';
            foreach ($lines as $line) {
                if (stripos($line, '.png') !== false && file_exists(trim($line))) {
                    $image_path = trim($line);
                    break;
                }
            }


          
            $comments_file = "C:/xampp/folder/htdocs/application_web/projet_python/web_data_comment.csv";
 
            if (file_exists($comments_file)) {
                $comments_content = file_get_contents($comments_file);
                echo "<h2>📝 Extracted Reddit Comments:</h2>";
                echo "<pre>" . htmlspecialchars($comments_content) . "</pre>";
            } else {
                echo "<p>⚠️ No Reddit comments found at: $comments_file</p>";
            }


           
            if (!empty($image_path) && file_exists($image_path)) {
               
                $relative_path = str_replace("C:/xampp/folder/htdocs/", "", $image_path);

                echo "<h2>📊 Visualization of Reddit Comments</h2>";
            
                echo "<img src='/$relative_path' alt='visualisation_web'>";
            } else {
                echo "<p><strong>❌ Error:</strong> Visualization not found.<br>Image path: $image_path</p>";
            }
        }
        ?>
    </div>
</body>
</html>