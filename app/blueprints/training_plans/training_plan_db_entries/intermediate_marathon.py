"""Script to create intermediate marathon training db."""
from ../models import IntermediateMarathon


week1 = IntermediateMarathon()
week1_dict = {
    "monday": 0,
    "tuesday": 3,
    "wednesday": 5,
    "thursday": 3,
    "friday": 0,
    "saturday": 5,
    "sunday": 8
}
week1.from_dict(week1_dict)
week1.save()

week2 = IntermediateMarathon()
week2_dict = {
    "monday": 0,
    "tuesday": 3,
    "wednesday": 5,
    "thursday": 3,
    "friday": 0,
    "saturday": 5,
    "sunday": 9
}
week2.from_dict(week2_dict)
week2.save()

week3 = IntermediateMarathon()
week3_dict = {
    "monday": 0,
    "tuesday": 3,
    "wednesday": 5,
    "thursday": 3,
    "friday": 0,
    "saturday": 5,
    "sunday": 6
}
week3.from_dict(week3_dict)
week3.save()

week4 = IntermediateMarathon()
week4_dict = {
    "monday": 0,
    "tuesday": 3,
    "wednesday": 6,
    "thursday": 3,
    "friday": 0,
    "saturday": 6,
    "sunday": 11
}
week4.from_dict(week4_dict)
week4.save()

week5 = IntermediateMarathon()
week5_dict = {
    "monday": 0,
    "tuesday": 3,
    "wednesday": 6,
    "thursday": 3,
    "friday": 0,
    "saturday": 6,
    "sunday": 12
}
week5.from_dict(week5_dict)
week5.save()

week6 = IntermediateMarathon()
week6_dict = {
    "monday": 0,
    "tuesday": 3,
    "wednesday": 5,
    "thursday": 3,
    "friday": 0,
    "saturday": 6,
    "sunday": 9
}
week6.from_dict(week6_dict)
week6.save()

week7 = IntermediateMarathon()
week7_dict = {
    "monday": 0,
    "tuesday": 4,
    "wednesday": 7,
    "thursday": 4,
    "friday": 0,
    "saturday": 7,
    "sunday": 14
}
week7.from_dict(week7_dict)
week7.save()

week8 = IntermediateMarathon()
week8_dict = {
    "monday": 0,
    "tuesday": 4,
    "wednesday": 7,
    "thursday": 4,
    "friday": 0,
    "saturday": 7,
    "sunday": 15
}
week8.from_dict(week8_dict)
week8.save()

week9 = IntermediateMarathon()
week9_dict = {
    "monday": 0,
    "tuesday": 4,
    "wednesday": 5,
    "thursday": 4,
    "friday": 0,
    "saturday": 0,
    "sunday": 13.1
}
week9.from_dict(week9_dict)
week9.save()

week10 = IntermediateMarathon()
week10_dict = {
    "monday": 0,
    "tuesday": 4,
    "wednesday": 8,
    "thursday": 4,
    "friday": 0,
    "saturday": 8,
    "sunday": 17
}
week10.from_dict(week10_dict)
week10.save()

week11 = IntermediateMarathon()
week11_dict = {
    "monday": 0,
    "tuesday": 5,
    "wednesday": 8,
    "thursday": 5,
    "friday": 0,
    "saturday": 8,
    "sunday": 18
}
week11.from_dict(week11_dict)
week11.save()

week12 = IntermediateMarathon()
week12_dict = {
    "monday": 0,
    "tuesday": 5,
    "wednesday": 5,
    "thursday": 5,
    "friday": 0,
    "saturday": 8,
    "sunday": 13
}
week12.from_dict(week12_dict)
week12.save()

week13 = IntermediateMarathon()
week13_dict = {
    "monday": 0,
    "tuesday": 5,
    "wednesday": 8,
    "thursday": 5,
    "friday": 0,
    "saturday": 5,
    "sunday": 20
}
week13.from_dict(week13_dict)
week13.save()

week14 = IntermediateMarathon()
week14_dict = {
    "monday": 0,
    "tuesday": 5,
    "wednesday": 5,
    "thursday": 5,
    "friday": 0,
    "saturday": 8,
    "sunday": 12
}
week14.from_dict(week14_dict)
week14.save()

week15 = IntermediateMarathon()
week15_dict = {
    "monday": 0,
    "tuesday": 5,
    "wednesday": 8,
    "thursday": 5,
    "friday": 0,
    "saturday": 5,
    "sunday": 20
}
week15.from_dict(week15_dict)
week15.save()

week16 = IntermediateMarathon()
week16_dict = {
    "monday": 0,
    "tuesday": 5,
    "wednesday": 6,
    "thursday": 5,
    "friday": 0,
    "saturday": 4,
    "sunday": 12
}
week16.from_dict(week16_dict)
week16.save()

week17 = IntermediateMarathon()
week17_dict = {
    "monday": 0,
    "tuesday": 4,
    "wednesday": 5,
    "thursday": 4,
    "friday": 0,
    "saturday": 3,
    "sunday": 8
}
week17.from_dict(week17_dict)
week17.save()

week18 = IntermediateMarathon()
week18_dict = {
    "monday": 0,
    "tuesday": 3,
    "wednesday": 4,
    "thursday": 0,
    "friday": 0,
    "saturday": 2,
    "sunday": 26.2
}
week18.from_dict(week18_dict)
week18.save()
