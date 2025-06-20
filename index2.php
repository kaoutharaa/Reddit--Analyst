<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
    <style>
        body {
            margin: 0;
            font-family: sans-serif;
            background-color: #181818;
            color: #e0e0e0;
        }

        .navigation-bar {
            background-color: #212121;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            padding: 15px 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .logo {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            background-color: #e0e0e0;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-right: 15px;
        }

        .logo svg {
            width: 70%;
            height: 70%;
            fill: #212121;
        }

        .nav-item {
            background-color: #333;
            color: #e0e0e0;
            padding: 10px 15px;
            border-radius: 8px;
            text-decoration: none;
            display: flex;
            align-items: center;
            margin-right: 10px;
            cursor: pointer;
            border: none;
            transition: background-color 0.3s ease;
        }

        .nav-item:hover {
            background-color: #555;
        }

        .nav-item svg {
            width: 20px;
            height: 20px;
            margin-right: 8px;
            fill: #e0e0e0;
        }

        .nav-item.clicked {
            border: 2px solid #64b5f6;
        }

        .research-options {
            display: flex;
            margin-left: 10px;
        }

        .research-option {
            background-color: #333;
            color: #e0e0e0;
            padding: 10px 15px;
            border-radius: 8px;
            text-decoration: none;
            display: flex;
            align-items: center;
            margin-right: 10px;
            cursor: pointer;
            border: none;
            transition: background-color 0.3s ease;
        }

        .research-option:hover {
            background-color: #555;
        }

        .search-button {
            background-color: #333;
            color: #e0e0e0;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            border: none;
            cursor: pointer;
            margin-left: auto;
            transition: background-color 0.3s ease;
        }

        .search-button:hover {
            background-color: #555;
        }

        .search-button svg {
            width: 20px;
            height: 20px;
            fill: #e0e0e0;
        }

        .dashboard-container {
            margin: 20px auto;
            padding: 20px;
            border-radius: 10px;
            background-color: #212121;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            width: 80%;
            max-width: 900px;
            position: relative;
        }

        #dashboard-table {
            display: none;
            border-collapse: collapse;
            width: 100%;
            background-color: #333;
            border: 1px solid #555;
            text-align: left;
            margin-top: 20px;
            border-radius: 8px;
            overflow: hidden;
        }

        #dashboard-table th, #dashboard-table td {
            padding: 12px 15px;
            border-bottom: 1px solid #555;
        }

        #dashboard-table th {
            background-color: #444;
            color: #f0f0f0;
        }

        #dashboard-table tr:last-child td {
            border-bottom: none;
        }

        #subreddit-form-container {
            display: none;
            background-color: #222;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            width: 500px;
            position: absolute;
            top: 100px;
            left: 10px;
            z-index: 10;
            animation: fadeIn 0.3s ease-in-out;
        
        }


        
        #post-form-container {
            display: none;
            background-color: #222;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            width: 500px;
            position: absolute;
            top: 100px;
            left: 10px;
            z-index: 10;
            animation: fadeIn 0.3s ease-in-out;
        
        }


        #subreddit-form-container label {
            margin-bottom: 5px;
            color: #eee;
            display: block;
        
        
        }

        
        #post-form-container label {
            margin-bottom: 5px;
            color: #eee;
            display: block;
        
        
        }

        #subreddit-form-container input[type="text"],
        #subreddit-form-container input[type="number"],
        #subreddit-form-container select,
        #subreddit-form-container button {
            padding: 10px;
            margin-bottom: 1px;
            border: 1px solid #444;
            border-radius: 4px;
            background-color: #333;
            color: white;
            box-sizing: border-box;
            width: 100%;
        
        
        }
        
        #post-form-container input[type="text"],
        #post-form-container input[type="number"],
        #post-form-container select,
        #post-form-container button {
            padding: 10px;
            margin-bottom: 1px;
            border: 1px solid #444;
            border-radius: 4px;
            background-color: #333;
            color: white;
            box-sizing: border-box;
            width: 100%;
        
        
        }

        #subreddit-form-container button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
            transition: background-color 0.3s ease;
        

        
        }

        #post-form-container button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
            transition: background-color 0.3s ease;
        

        }
        #subreddit-form-container button:hover {
            background-color: #0056b3;
        }
        #post-form-container button:hover {
            background-color: #0056b3;
        }
        @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    #subreddit-form-container,
    #dashboard-container,
    #post-form-container {
        animation: fadeIn 0.3s ease-in-out;
    }

    /* Add this CSS for the animation */
    #dashboard-table tr {
        animation: slideIn 0.5s ease-out;
    }

    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateX(-20px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    </style>
</head>
<body>

    <div class="navigation-bar">
        <div class="logo">
            <svg viewBox="0 0 24 24">
                <path d="M12 4C9.79 4 8 5.79 8 8V16C8 18.21 9.79 20 12 20C14.21 20 16 18.21 16 16V8C16 5.79 14.21 4 12 4M10 8H14V16H10V8Z" />
            </svg>
        </div>

        <a href="#" class="nav-item">
            <svg viewBox="0 0 24 24">
                <path d="M12 4C10.9 4 10 4.9 10 6V18C10 19.1 10.9 20 12 20C13.1 20 14 19.1 14 18V6C14 4.9 13.1 4 12 4M6 8V16C6 17.1 6.9 18 8 18V6C8 4.9 6.9 4 6 4V8M16 8V16C16 17.1 16.9 18 18 18V6C18 4.9 16.9 4 16 4V8Z" />
            </svg>
            Research
        </a>

        <div id="byPostButton" class="research-options">
            <button class="research-option" data-form="post">
                <svg viewBox="0 0 24 24">
                    <path d="M17 18C15.89 18 15 17.11 15 16V5C15 3.89 15.89 3 17 3H19C20.11 3 21 3.89 21 5V16C21 17.11 20.11 18 19 18H17M11 18C9.89 18 9 17.11 9 16V9C9 7.89 9.89 7 11 7H13C14.11 7 15 7.89 15 9V16C15 17.11 14.11 18 13 18H11M6 18C4.89 18 4 17.11 4 16V12C4 10.89 4.89 10 6 10H8C9.11 10 10 10.89 10 12V16C10 17.11 9.11 18 8 18H6Z" />
                </svg>
                By Post
            </button>
            <button id="bySubredditButton" class="research-option" data-form="subreddit">
                <svg viewBox="0 0 24 24">
                    <path d="M20 6H12L10 4H4C2.9 4 2 4.9 2 6V18C2 19.1 2.9 20 4 20H20C21.1 20 22 19.1 22 18V6M20 18H4V8H20V18M18 10V12H6V10H18M16 14V16H8V14H16Z" />
                </svg>
                By Subreddit
            </button>
        </div>

        <div id="dashboardButton" class="nav-item">
            <svg viewBox="0 0 40 40">
                <path d="M19 3H5C3.9 3 3 3.9 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.9 20.1 3 19 3M19 19H5V5H19V19M10 17L5 12L6.41 10.59L10 14.17L17.59 6.59L19 8L10 17Z" />
            </svg>
            Dashboard
        </div>

        <button class="search-button">
            <svg viewBox="0 0 24 24">
                <path d="M15.5 14H14.71L14.43 13.73C15.41 12.59 16 11.11 16 9.5C16 5.91 13.09 3 9.5 3C5.91 3 3 5.91 3 9.5C3 13.09 5.91 16 9.5 16C11.11 16 12.59 15.41 13.73 14.43L14 14.71V15.5L19 20L20.5 18.5L15.5 14M9.5 14C7.01 14 5 11.99 5 9.5C5 7.01 7.01 5 9.5 5C11.99 5 14 7.01 14 9.5C14 11.99 11.99 14 9.5 14Z" />
            </svg>
        </button>
    </div>

    <div class="dashboard-container">
        <table id="dashboard-table">
            <tr>
                <th>Metric</th>
                <th>Value</th>
            </tr>
            <?php
            $json_data = file_get_contents('C:/xampp/folder/htdocs/application_web/projet_python/stats.json');
            $stats = json_decode($json_data, true);
            foreach ($stats as $key => $value):
            ?>
                <tr>
                    <td><?= str_replace("_", " ", $key) ?></td>
                    <td><?= $value ?></td>
                </tr>
            <?php endforeach; ?>
        </table>

        <div id="subreddit-form-container">
            <form id="subredditForm" action="process.php" method="POST">
                <label for="analyzed_subreddits">Choose a subreddit</label>
                <input type="text" id="analyzed_subreddits" name="analyzed_subreddits" required>

                <label for="comments-per-post">Number of comments to fetch</label>
                <input type="number" id="comments-per-post" name="comments-per-post" value="comments_per_post" min="0" max="100">

                <button type="submit">Enter</button>
            </form>
        </div>
        <div id="post-form-container">
            <form id="postForm" action="process.php" method="POST">
                <label for="analyzed_post">Choose a Post</label>
                <input type="text" id="analyzed_post" name="analyzed_post" required>

                <label for="comments-per-post">Number of comments to fetch</label>
                <input type="number" id="comments-per-post" name="comments-per-post" value="comments_per_post" min="0" max="100">

                <button type="submit">Enter</button>
            </form>
        </div>


    </div>

    <script>
        const dashboardButton = document.getElementById('dashboardButton');
        const dashboardTable = document.getElementById('dashboard-table');
        const navItems = document.querySelectorAll('.nav-item');
        const researchOptions = document.querySelector('.research-options');
        const researchNavItem = document.querySelector('.nav-item:nth-child(2)');
        const bySubredditButton = document.getElementById('bySubredditButton');
        const subredditFormContainer = document.getElementById('subreddit-form-container');
        const byPostButton = document.getElementById('byPostButton');
        const postFormContainer = document.getElementById('post-form-container');
        const researchOptionsButtons = document.querySelectorAll('.research-option');


        researchOptions.style.display = 'none';
        subredditFormContainer.style.display = 'none';
        dashboardTable.style.display = 'table';
        postFormContainer.style.display = 'none';

        function hideAllForms() {
            subredditFormContainer.style.display = 'none';
            postFormContainer.style.display = 'none';
        }

        researchNavItem.addEventListener('click', function() {
            researchOptions.style.display = researchOptions.style.display === 'flex' ? 'none' : 'flex';
            navItems.forEach(item => {
                item.classList.remove('clicked');
            });
            this.classList.add('clicked');
            dashboardTable.style.display = 'none';
            hideAllForms();
        });

        researchOptionsButtons.forEach(button => {
            button.addEventListener('click', function() {
                const formType = this.dataset.form;
                hideAllForms();
                if (formType === 'subreddit') {
                    subredditFormContainer.style.display = 'block';
                } else if (formType === 'post') {
                    postFormContainer.style.display = 'block';
                }
                document.querySelectorAll('.research-option').forEach(option => {
                    option.classList.remove('clicked');
                });
                this.classList.add('clicked');
                dashboardTable.style.display = 'none';
            });
        });

        dashboardButton.addEventListener('click', function() {
            dashboardTable.style.display = 'table';
            navItems.forEach(item => {
                item.classList.remove('clicked');
            });
            this.classList.add('clicked');
            researchOptions.style.display = 'none';
            hideAllForms();
        });

        document.addEventListener('click', function(event) {
            const navigationBar = document.querySelector('.navigation-bar');
            const dashboardContainer = document.querySelector('.dashboard-container');

            if (!navigationBar.contains(event.target) && !dashboardContainer.contains(event.target)) {
                navItems.forEach(item => {
                    item.classList.remove('clicked');
                });
                researchOptions.style.display = 'none';
                hideAllForms();
            }
        });
    </script>
</body>
</html>
