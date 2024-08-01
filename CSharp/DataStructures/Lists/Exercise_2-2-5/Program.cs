// Exercise 2-2-5
// Lists with different Datatypes are not allowed in C#, but
// we can write the numbers as strings to a string List
String[] arr = new string[] { "10", "25", "30", "45", "90", "ab", "cd", "ef" };
List<string> lst = new List<string>();
foreach (string str in arr)
{
    lst.Add(str);
}
foreach (string str in lst)
{
    Console.Write(str + " ");
}
