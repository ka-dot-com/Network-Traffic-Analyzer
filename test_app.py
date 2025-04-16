import unittest
import numpy as np
from app import capture_packets

class TestCapturePackets(unittest.TestCase):
    def test_packet_capture(self):
        packets = capture_packets()
        self.assertEqual(packets.shape, (1, 50))  # Expecting shape (1, 50)
        self.assertTrue((packets >= 0).all())  # All sizes should be non-negative

if __name__ == "__main__":
    unittest.main()