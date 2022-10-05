function validateForm(buttonname)
{
    var myForm = document.getElementById("speciesform");
    if ((myForm["name"].value == "" || myForm["genus"].value == "" || myForm["max_age"].value == "" ||
        myForm["region"].value == "" || myForm["average_size"].value == "") && buttonname != "deletebutton" )
    {
        alert("All fields must contain values!");
        return false;
    }
    else
    {
        myForm.method = "post";

        if(buttonname == "createbutton")
            myForm.action = "/create";
        if(buttonname == "deletebutton")
            myForm.action = "/delete"
        if(buttonname == "updatebutton")
            myForm.action = "/update"

        myForm.submit();
        myForm.reset();
    }

    return false;
}

function enterKeyPressed(event)
{
    if (event.keyCode == 13)
    {
        alert("WOAH");
    }
}