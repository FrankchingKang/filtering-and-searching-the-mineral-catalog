from django.test import TestCase

# Create your tests here.

from .models import Minerals
from django.urls import reverse

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
groups = ['Silicates', 'Oxides', 'Sulfates', 'Sulfides', 'Carbonates',
          'Halides', 'Sulfosalts', 'Phosphates', 'Borates',
          'Organic Minerals', 'Arsenates', 'Native Elements', 'Other']


class MineralModelTests(TestCase):
    def test_mineral_creation(self):
        mineral = Minerals.objects.create(
            name = "test mineral",
            color = "red"
        )
        self.assertEqual("test mineral", mineral.name)
        self.assertEqual("", mineral.luster)



class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Minerals.objects.create(
            #name = "test_mineral_one",
            name = "Apple",
            color = "Red",
        )
        self.mineral2 = Minerals.objects.create(
            name = "Banana",
            color = "Yellow",
        )
        self.mineral3 = Minerals.objects.create(
            name = "Test Name",
            image_filename = "testname.jbp",
            image_caption = "",
            category = "Sulfides and Sulfosalts",
            formula = "<sub>1</sub>,<sub>066</sub>.<sub>44</sub> g/mol",
            strunz_classification = "test strun",
            crystal_system  = 'test crystal crystal',
            unit_cell = " test unit",
            crystal_symmetry = " test crystal_symmetry",
            cleavage = "test cleavage",
            mohs_scale_hardness = "test mohs_scale_hardness",
            luster = "test luster",
            streak = "Test Streak",
            diaphaneity = "test diap",
            optical_properties = "test optical_properties",
            refractive_index = "test refractive",
            crystal_habit = "test crystal",
            specific_gravity = "test specific_gravity",
            group = "Test Group",
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                        kwargs={'pk':self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral.color)
        self.assertContains(resp, self.mineral.name)
        resp2 = self.client.get(reverse('minerals:detail',
                                        kwargs={'pk':self.mineral2.pk}))
        self.assertEqual(resp2.status_code, 200)
        self.assertEqual(self.mineral2, resp2.context['mineral'])
        self.assertTemplateUsed(resp2, 'minerals/detail.html')
        self.assertContains(resp2, self.mineral2.color)
        self.assertContains(resp2, self.mineral2.name)

        resp3 = self.client.get(reverse('minerals:detail',
                                        kwargs={'pk':self.mineral3.pk}))
        self.assertEqual(resp3.status_code, 200)
        self.assertEqual(self.mineral3, resp3.context['mineral'])
        self.assertTemplateUsed(resp3, 'minerals/detail.html')
        self.assertContains(resp3, self.mineral3.color)
        self.assertContains(resp3, self.mineral3.unit_cell)
        self.assertContains(resp3, self.mineral3.name)
        self.assertContains(resp3, self.mineral3.image_filename)
        self.assertContains(resp3, self.mineral3.streak)
        self.assertContains(resp3, self.mineral3.specific_gravity)
        self.assertContains(resp3, self.mineral3.group)
        self.assertContains(resp3, self.mineral3.refractive_index)

    def test_mineral_random_view(self):
        resp = self.client.get(reverse('minerals:random'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/detail.html')

    def test_mineral_alpha_list_view(self):
        resp = self.client.get(reverse('minerals:alpha_list',
                                        kwargs={'letter': 'B'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertIn(self.mineral2, resp.context['minerals'])
        self.assertNotIn(self.mineral3, resp.context['minerals'])

    def test_search_view(self):
        resp = self.client.get(reverse('minerals:search'), {'q': 'Apple'})
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertIn(self.mineral, resp.context['minerals'])

    def test_mineral_group_list_view(self):
        resp = self.client.get(reverse('minerals:group_list',
                                        kwargs={'group': 'Test Group'}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertNotIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral3, resp.context['minerals'])
