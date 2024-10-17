#!C:/xampp/perl/bin/perl.exe
use strict;
use warnings;
use CGI;

# Create a new CGI object
my $cgi = CGI->new;

# Get the form values
my $num1 = $cgi->param('num1');
my $num2 = $cgi->param('num2');
my $operation = $cgi->param('operation');
my $result;
my $error;

# Check if inputs are numeric
if ($num1 !~ /^-?\d+(\.\d+)?$/ || $num2 !~ /^-?\d+(\.\d+)?$/) {
    $error = "Please enter valid numbers.";
} else {
    # Perform the selected operation
    if ($operation eq 'add') {
        $result = $num1 + $num2;
    } elsif ($operation eq 'subtract') {
        $result = $num1 - $num2;
    } elsif ($operation eq 'multiply') {
        $result = $num1 * $num2;
    } elsif ($operation eq 'divide') {
        if ($num2 == 0) {
            $error = "Error: Division by zero is not allowed.";
        } else {
            $result = $num1 / $num2;
        }
    } else {
        $error = "Invalid operation.";
    }
}

# Output the HTML content
print $cgi->header('text/html');
print <<HTML;
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculation Result</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 50px;
            background-color: #f4f4f9;
            text-align: center;
        }
        .result, .error {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 300px;
            display: inline-block;
        }
        .error {
            color: red;
        }
        a {
            display: inline-block;
            margin-top: 20px;
            background-color: #007bff;
            color: white;
            padding: 12px 20px;
            text-decoration: none;
            border-radius: 20px;
        }
        a:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Calculation Result</h1>
HTML

if ($error) {
    print "<div class='error'><strong>Error:</strong> $error</div>";
} else {
    print "<div class='result'><p>The result of $operation $num1 and $num2 is: $result</p></div>";
}

print <<HTML;
    <br/><a href="/calculator.html">Perform Another Calculation</a>
</body>
</html>
HTML
