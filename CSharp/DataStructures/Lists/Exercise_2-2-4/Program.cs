// Exercise 2-2-4
// without count
List<int> lst = new List<int> { 3, 2, 2, 1, 9, 1, 2, 3, 7 };
int counter = 0;
foreach (var item in lst)
{
    counter++;
}
Console.Write(counter);

Console.WriteLine("\n---");

// with count
int count = lst.Count();
Console.Write(count);

