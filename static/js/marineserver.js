function validateForm()
{
    var myForm = document.getElementById("speciesform");
    if (myForm["name"].value == "" || myForm["genus"].value == "" || myForm["max_age"].value == "" ||
        myForm["region"].value == "" || myForm["average_size"].value == "")
    {
        alert("All fields must contain values!");
        return false;
    }

    myForm.submit();
    myForm.reset();
    return false;
}