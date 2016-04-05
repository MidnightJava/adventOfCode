package test;


import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static java.util.stream.Collectors.*;

/**
 * 
 * from https://dzone.com/articles/transforming-collections-java-8-collectors-api
 *
 */

public class CollectorsDemo {
	
	public static class Person {
	    private Integer age;
	    private String name;

	    @Override
	    public String toString() {
	        return "Person{" +
	                "age=" + age +
	                ", name='" + name + '\'' +
	                '}';
	    }

	    public Person(Integer age, String name) {
	        this.age = age;
	        this.name = name;
	    }

	    public Integer getAge() {
	        return age;
	    }

	    public void setAge(Integer age) {
	        this.age = age;
	    }

	    public String getName() {
	        return name;
	    }

	    public void setName(String name) {
	        this.name = name;
	    }
	}
	
    public static void main(String[] args) {
        List<Person> people = initPeople();
        toCollections(people);
        joining(people);
        summing(people);
        partitioningBy(people);
        groupingBy(people);
        maxBy(people);
        collectingAndThen(people);
    }

    private static List<Person> initPeople() {
        return IntStream.rangeClosed(1, 200)
                .mapToObj(integer -> new Person(integer, "name_" + integer))
                .collect(Collectors.toList());
    }

    private static void toCollections(List<Person> people) {
        final List<Person> toList = people.stream()
                .collect(toList());
        System.out.println(toList);

        final Set<Person> toSet = people.stream()
                .collect(toSet());
        System.out.println(toSet);

        final ArrayList<Person> arrayList = people.stream()
                .collect(toCollection(ArrayList<Person>::new));
        System.out.println(arrayList);

        final HashSet<Person> hashSet = people.stream()
                .collect(toCollection(HashSet<Person>::new));
        System.out.println(hashSet);
    }

    private static void joining(List<Person> people) {
        final String joinedWithoutDelimiter = people.stream()
                .map(String::valueOf)
                .collect(Collectors.joining());

        System.out.format("joinedWithoutDelimiter: %s%n", joinedWithoutDelimiter);

        final String joinedWithDelimiter = people.stream()
                .map(String::valueOf)
                .collect(Collectors.joining("-"));

        System.out.format("joinedWithDelimiter: %s%n", joinedWithDelimiter);

        final String delimiterPrefixAndSuffix = people.stream()
                .map(String::valueOf)
                .collect(Collectors.joining("-", "prefix", "suffix"));

        System.out.format("delimiterPrefixAndSuffix: %s%n", delimiterPrefixAndSuffix);
    }

    private static void summing(List<Person> people) {
        final Integer summedAge = people.stream()
                .collect(summingInt(Person::getAge));

        System.out.format("summedAge: %d%n", summedAge);

        final IntSummaryStatistics ageSummaryStatistics = people.stream()
                .collect(summarizingInt(Person::getAge));

        System.out.format("ageSummaryStatistics.getAverage(): %f%n", ageSummaryStatistics.getAverage());
        System.out.format("ageSummaryStatistics.getMax(): %d%n", ageSummaryStatistics.getMax());
        System.out.format("ageSummaryStatistics.getMin(): %d%n", ageSummaryStatistics.getMin());
        System.out.format("ageSummaryStatistics.getSum(): %d%n", ageSummaryStatistics.getSum());
    }

    private static void partitioningBy(List<Person> people) {
        final Map<Boolean, List<Person>> partitions = people.stream()
                .collect(Collectors.partitioningBy(person -> person.getAge() >= 18));

        System.out.println("Total people that can vote:" + partitions.get(Boolean.TRUE).stream().count());
        System.out.println("Total people that can't vote:" + partitions.get(Boolean.FALSE).stream().count());
    }

    private static void groupingBy(List<Person> people) {
        final Map<Integer, List<Person>> mapWithPersonNameLengthAsKey = people.stream()
                .collect(Collectors.groupingBy(person -> person.getName().length()));
        System.out.println(mapWithPersonNameLengthAsKey);

        final Map<String, List<Person>> mapWithYoungOrOldAsKey = people.stream()
                .collect(Collectors.groupingBy(person -> (person.getAge() > 50) ? "old" : "young"));

        System.out.format("Number of age groups: %d%n", mapWithYoungOrOldAsKey.keySet().size());
        System.out.println(mapWithYoungOrOldAsKey);
    }

    private static void maxBy(List<Person> people) {
        final Optional<Person> firstPersonWithMaxNameLength = people.stream()
                .collect(Collectors.maxBy((p1, p2) -> {
                    final int p1NameLength = p1.getName().length();
                    final int p2NameLength = p2.getName().length();
                    return p1NameLength - p2NameLength;
                }));
        firstPersonWithMaxNameLength.ifPresent(System.out::println);
    }

    private static void collectingAndThen(List<Person> people) {
        try {
            final List<Person> unmodifiableList = people.stream()
                    .collect(Collectors.collectingAndThen(toList(), Collections::unmodifiableList));
            unmodifiableList.add(new Person(2, "name"));
        } catch (UnsupportedOperationException ex) {
            ex.printStackTrace();
        }
    }
}


