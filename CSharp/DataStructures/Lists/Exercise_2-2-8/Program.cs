// Exercise 2-2-8
// In C# mixed Datatype lists are not allowed for this Exercise we
// will use lists with integer numbers only
List<int> lst_one = new List<int> { 9, 8, 7, 14, 3, 2 };
List<int> lst_two = new List<int> { 1, 9, 6, 3, 9 };
lst_one.AddRange(lst_two);
List<int> distinct = lst_one.Distinct().ToList();

foreach (int i in distinct)
{
    Console.Write(i + " ");
}