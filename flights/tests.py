"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import Client, TestCase

from .models import Airport, Flight, Passenger

# TODO: Configure your database in settings.py and sync before running tests.

class SimpleTest(TestCase):
    """Tests for the application views."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(SimpleTest, cls).setUpClass()
        django.setup()

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """

class FlightTestCase(TestCase):
    def setUp(self):
        # creare Airports 
        a1=Airport.objects.create(code="AAA", city="City A")
        a2=Airport.objects.create(code="BBB", city="City B")

        # create flights

        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(),3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(),1)

    def test_valid_flight(self):
        a1= Airport.objects.get(code="AAA")
        a2= Airport.objects.get(code="BBB")
        f = Flight.objects_get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_destination(self):
        a1 = Airport.objects.get(code="AAA")
        f= Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())

        
    def test_invalid_flight_duration(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f= Flight.objects.get(origin=a1, destination=a1, duration=-100)
        self.assertFalse(f.is_valid_flight())


  