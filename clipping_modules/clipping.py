import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from scenedetect import detect, ContentDetector, split_video_ffmpeg


class ClippingModule:
    def __init__(self, path_to_video_out, window=30, technique='fixed'):
        """
        path_to_video_out: Directory where clips will be saved.
        window: Size of cut in seconds (only necessary when technique='fixed').
        technique: Options are 'fixed' or 'scene'
        """
        self.window = window
        self.path_to_video_out = path_to_video_out
        self.technique = technique

    def get_length(self, filename):
        result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                                 "format=duration", "-of",
                                 "default=noprint_wrappers=1:nokey=1", filename],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
        return float(result.stdout)

    def divide_video(self, input_path, name):
        """
        Executes fixed-time clipping.
        
        input_path: Location of the video that will be clipped.
        name: The name or id of the video (usually the YouTube ID).
         
        Clips will be stored in the 'self.path_to_video_out' directory and 
            named with the format {name}&{i}.mp4, where i is the clip start time.
        """
        
        for i in range(0, int(round(self.get_length(input_path), 0)), self.window):
            ffmpeg_extract_subclip(input_path, i, i + self.window,
                                   targetname=self.path_to_video_out + f'/{name}@{i}.mp4')

    def divide_video_SceneD(self, input_path, name):
        scene_list = detect(input_path, ContentDetector())
        split_video_ffmpeg(
            input_video_path=input_path, 
            scene_list=scene_list, 
            video_name=name, 
            output_file_template=f'{self.path_to_video_out}/$VIDEO_NAME@$SCENE_NUMBER.mp4'
        )
        
    def get_scenes_pyscene(self, input_path, name):
        output_path = self.path_to_video_out
        """
        !scenedetect \
            -i $input_path \
            -o $output_path \
            --min-scene-len 00:00:10.0 \
            detect-content \
            split-video 
        """
        pass

    def get_clips(self, input_path, name):
        if self.technique == 'fixed':
            self.divide_video(input_path, name)
        else:
            self.divide_video_SceneD(input_path, name)
