List<int> lst = new List<int> { };
for (int i = 1; i < 11; i++)
{
    lst.Add(i);
}
foreach (int i in lst)
{
    Console.Write(i + " ");
}