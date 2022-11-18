import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from scenedetect import detect, ContentDetector, split_video_ffmpeg


class ClippingModule:
    def __init__(self, path_to_video_in, path_to_video_out, window=30, technique='fixed'):
        self.window = 30
        self.path_to_video_in = path_to_video_in
        self.path_to_video_out = path_to_video_out
        self.technique = technique

    def get_length(self, filename):
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "format=duration", "-of",
                                 "default=noprint_wrappers=1:nokey=1", filename],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        return float(result.stdout)

    def divide_video(self):
        for i in range(0, int(round(self.get_length(self.path_to_video_in), 0)), self.window):
            ffmpeg_extract_subclip(self.path_to_video_in, i, i + self.window,
                                   targetname=self.path_to_video_out + "/part" + str(i) + ".mp4")

    def divide_video_SceneD(self):
        scene_list = detect(self.path_to_video_in, ContentDetector())
        split_video_ffmpeg(self.path_to_video_in, scene_list, video_name=self.path_to_video_out + '/')

    def get_clips(self):
        if self.technique == 'fixed':
            self.divide_video()
        else:
            self.divide_video_SceneD()

    def ejemplo(self):
        return {
            "video_id": "fnuaiownuoa",
            "clip_id": 0,
            "captions": [],
            "duration": 0
        }


