List<int> lst = new List<int> { 6, 8, 3, 4, 1, 12, 2, 9, 2 };
List<int> new_list = new List<int> { };

foreach (int i in lst)
{
    new_list.Add(i);
    new_list.Sort();
}
foreach (int i in new_list)
{
    Console.Write(i + " ");
}