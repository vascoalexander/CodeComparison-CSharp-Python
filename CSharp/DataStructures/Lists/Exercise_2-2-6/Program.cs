// Exercise 2-2-6
List<int> lst = new List<int>();
List<int> new_lst = new List<int>();
for (int i = 1; i < 11; i++)
{
    lst.Add(i);
}
foreach (int i in lst)
{
    if (i % 3 == 1)
    {
        new_lst.Add(i);
    }
}
foreach (int i in new_lst)
{
    Console.Write(i + " ");
}

