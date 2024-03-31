Simple Python application for testing image annotation and reasoning using the LLAVA open-source LLM. 

This example is a docker version of the tutorail discribed in this video: https://www.youtube.com/watch?v=_TUvb6NtpGA

To run this demo simply follow these steps:

1. Install Ollama locally: (https://ollama.ai/)
2. Install the latest version of the Llava LLM: `ollama run llava`
3. Build the docker container: `docker build . -t annotator`
4. Run the docker container: `docker run -i -t annotator`

If everything works well and the LLM gods are on your side you should see something like this output to the console:


```markdown
Processing ./images/Screen Shot 2018-03-22 at 6.31.34 PM.png

 Description:
The image is a black and white photograph of a man standing next to a vintage radio device. He appears to be demonstrating the operation or features of the device, as suggested by his posture and attention towards the radio.

Visible Objects:
1. Large metal horn-like structures on either side of the radio, resembling speakers or sound amplifiers.
2. The man is standing beside a tripod with two microphones on it.
3. The person is dressed in casual attire, and their face is visible, showing them engaged with the device.
4. The background is nondescript, with no distinguishable landmarks or architecture, providing a focus on the radio equipment and the man.

Notable Details:
1. The image has a vintage feel due to its monochromatic color scheme and the style of the radio device.
2. There are no visible texts within the image that can be confidently read.
3. The setting appears to be an open outdoor space, with the man standing on what looks like a sandy surface.
4. There is no NSFW content detected in this image.

NSFW Content Detected: No 
Processing ./images/boxes.png

 Description:
The image depicts a large group of people holding up boxes over their heads. The boxes have cardboard on the bottom, and the text "THE BOXES OF CARDBOARD CITY" is visible on them. The people are standing close together in what appears to be an outdoor setting.

Visible Objects:
1. Cardboard boxes being held above people's heads
2. People of various ages and genders, all participating in the box-holding activity
3. A clear sky suggesting good weather conditions
4. The ground beneath the group and their boxes

Notable Details:
1. The event seems to be a public demonstration or performance, given the scale and the unified action of holding up boxes.
2. The text on the boxes suggests that this might be part of an art installation, publicity stunt, or awareness campaign related to "Cardboard City."
3. The outdoor setting implies that this event is taking place during daylight hours with ample natural light.
4. There is no NSFW content detectable in the image.

NSFW Content Detected: No %
```