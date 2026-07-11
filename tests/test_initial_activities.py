import unittest

from src.backend.database import initial_activities


class InitialActivitiesTest(unittest.TestCase):
    def test_manga_maniacs_activity_is_seeded(self):
        self.assertIn("Manga Maniacs", initial_activities)

        manga_maniacs = initial_activities["Manga Maniacs"]

        self.assertEqual(
            manga_maniacs["description"],
            "Explore the fantastic stories of the most interesting characters from Japanese Manga (graphic novels).",
        )
        self.assertEqual(manga_maniacs["schedule"], "Tuesdays at 7:00 PM")
        self.assertEqual(
            manga_maniacs["schedule_details"],
            {
                "days": ["Tuesday"],
                "start_time": "19:00",
                "end_time": "20:00",
                "use_custom_schedule_text": True,
            },
        )
        self.assertEqual(manga_maniacs["max_participants"], 15)
        self.assertEqual(manga_maniacs["participants"], [])


if __name__ == "__main__":
    unittest.main()
