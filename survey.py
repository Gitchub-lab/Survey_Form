# surveyform.html

import webbrowser

f = open('surveyform.html', 'w')

html = """
<!doctype html>
<html lang="en">

    <head>

        <!-- CSS file for surveyform.html -->
            <link rel="stylesheet" href="css_survey.css">
    </head>

    <body>
     <h1 id="title">This is an exercise from freecodecamp.org
     <br>Select Survey Form from the Test Suite</h1>
            <br><br>
        <main id="main">           
            <h1 id="title">Survey Form</h1>
                <p id="description">Please fill out the form below.
                <form id="survey-form">
                    <label id="name-label"> Name<br> <input id="name" type="text" placeholder="Joe Smith" required>
                    </label>
                    <br>
                    <label id="email-label"> Email<br> <input id="email" type="email" placeholder="joesmith@email.com" required>
                    </label>
                    <br>
                    <label id="number-label"> Number<br> <input id="number" type="number" placeholder="1-10" required min=0 max=10>
                    </label>
                    <br>
                    
                    <label for="preference"> Choose a preference</label>
                    <select name="preference" id="dropdown">
                    <optgroup>
                    <option value="cold">Cold </option>
                    <option value="hot">Hot </option>
                    </optgroup>
                    </select>
                    <br>
                <label> <input type="radio" name="question" value="yes" checked> Yes</label>
                <label> <input type="radio" name="question" value="no"> No </label>
                    <br>
                    <br>
                <label>Which Color?<br> <input type="checkbox" name="choices" value="red" checked> Red </label>
                    <br>
                    <br>
                <label> <input type="checkbox" name="choices" value="blue"> Blue </label>
                    <br>
                    <br>
                <label> <input type="checkbox" name="choices" value="yellow"> Yellow </label>
                    <br>
                    <br>
                    <label> Comments</label>
                    <br>
                    <textarea name="comments">
                    </textarea>
                    <br>
                    <br>
                    <button id="submit" type="submit"> Submit</button>
                </form>
                </p>
                
            
            
        </main>
        
           <script src="https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js"></script>
    </body>

</html>
    
  """

f.write(html)
f.close()

webbrowser.open_new_tab('surveyform.html')
