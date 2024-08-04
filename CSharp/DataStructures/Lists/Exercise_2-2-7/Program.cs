// Exercise 2-2-7
string c = "Frankreich".ToLower();
char[] arr = c.ToCharArray();
Array.Sort(arr);

string sortedString = new string(arr);

Console.WriteLine(sortedString);
