import csv
from constants import *
from game.casting.animation import Animation
from game.casting.ghost import Ghost
from game.casting.cherry import Cherry
from game.casting.body import Body
from game.casting.wall import Wall
from game.casting.pellet import Pellet
from game.casting.path import Path
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.pacman import Pacman
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_pellets_action import CollidePelletsAction
from game.scripting.collide_ghost_action import CollideGhostAction
from game.scripting.control_pacman_action import ControlPacmanAction
from game.scripting.control_ghost_action import ControlGhostAction
from game.scripting.draw_ghost_action import DrawGhostAction
from game.scripting.draw_bg_action import DrawBGAction
from game.scripting.draw_pellets_action import DrawPelletsAction
from game.scripting.draw_cherry_action import DrawCherryAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_pacman_action import DrawPacmanAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ghost_action import MoveGhostAction
from game.scripting.move_pacman_action import MovePacmanAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_PELLETS_ACTION = CollidePelletsAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_GHOST_ACTION = CollideGhostAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_PACMAN_ACTION = ControlPacmanAction(KEYBOARD_SERVICE, PHYSICS_SERVICE)
    CONTROL_GHOST_ACTION = ControlGhostAction(PHYSICS_SERVICE)
    DRAW_GHOST_ACTION = DrawGhostAction(VIDEO_SERVICE)
    DRAW_BG_ACTION = DrawBGAction(VIDEO_SERVICE)
    DRAW_PELLETS_ACTION = DrawPelletsAction(VIDEO_SERVICE)
    DRAW_CHERRY_ACTION = DrawCherryAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_PACMAN_ACTION= DrawPacmanAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_GHOST_ACTION = MoveGhostAction()
    MOVE_PACMAN_ACTION = MovePacmanAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    change = ""

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_pellet(cast)
        self._add_cherry(cast)
        self._add_path(cast)
        self._add_background(cast)
        self._add_pacman(cast, Point(210, 362))
        self._add_ghost(cast, "Blinky", BLINKY_IMAGES, Point(210, 170))
        self._add_ghost(cast, "Pinky", PINKY_IMAGES, Point(210, 229))
        self._add_ghost(cast, "Inky", INKY_IMAGES, Point(178, 229))
        self._add_ghost(cast, "Clyde", CLYDE_IMAGES, Point(242, 229))
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        cast.clear_actors(GHOST_GROUP)
        self._add_ghost(cast, "Blinky", BLINKY_IMAGES, Point(210, 170))
        self._add_ghost(cast, "Pinky", PINKY_IMAGES, Point(210, 229))
        self._add_ghost(cast, "Inky", INKY_IMAGES, Point(178, 229))
        self._add_ghost(cast, "Clyde", CLYDE_IMAGES, Point(242, 229))
        self._add_pellet(cast)
        self._add_cherry(cast)
        self._add_pacman(cast, Point(210, 362))
        self._add_path(cast)
        self._add_background(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)


        script.clear_actions(INPUT)
        self.change = script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        cast.clear_actors(GHOST_GROUP)
        self._add_pacman(cast, Point(210, 362))
        self._add_ghost(cast, "Blinky", BLINKY_IMAGES, Point(210, 170))
        self._add_ghost(cast, "Pinky", PINKY_IMAGES, Point(210, 229))
        self._add_ghost(cast, "Inky", INKY_IMAGES, Point(178, 229))
        self._add_ghost(cast, "Clyde", CLYDE_IMAGES, Point(242, 229))
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_ghosts(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_PACMAN_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        cast.clear_actors(GHOST_GROUP)
        self._add_pacman(cast, Point(210, 362))
        self._add_ghost(cast, "Blinky", BLINKY_IMAGES, Point(210, 170))
        self._add_ghost(cast, "Pinky", PINKY_IMAGES, Point(210, 229))
        self._add_ghost(cast, "Inky", INKY_IMAGES, Point(178, 229))
        self._add_ghost(cast, "Clyde", CLYDE_IMAGES, Point(242, 229))
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------
    
    def _activate_ghosts(self, cast):
        for ghost in cast.get_actors(GHOST_GROUP):
            ghost.release()

    def _add_ghost(self, cast, name, image_group, pos):
        size = Point(GHOST_WIDTH, GHOST_HEIGHT)
        velocity = Point(0, 0)
        position = Point(pos.get_x() + FIELD_LEFT, pos.get_y() + FIELD_TOP)
        body = Body(position, size, velocity)
        animations = []
        animations.append(Animation(image_group["up"], GHOST_RATE))
        animations.append(Animation(image_group["right"], GHOST_RATE))
        animations.append(Animation(image_group["down"], GHOST_RATE))
        animations.append(Animation(image_group["left"], GHOST_RATE))
        ghost = Ghost(body, name, animations)
        cast.add_actor(GHOST_GROUP, ghost)
        
    def _add_path(self, cast):
        cast.clear_actors(PATH_GROUP)

        with open(PATH_FILE, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            for r, row in enumerate(reader):
                
                number = int(row[0])
                x, y, direction = int(row[1]) + FIELD_LEFT, int(row[2]) + FIELD_TOP, str(row[3])
                directions = []
                for i in range(len(direction)):
                    directions.append(direction[i])
                position = Point(x, y)
                size = Point(PATH_WIDTH, PATH_HEIGHT)
                velocity = Point(0, 0)

                body = Body(position, size, velocity)

                path = Path(body, directions, number)
                cast.add_actor(PATH_GROUP, path)
    
    def _add_pellet(self, cast):
        cast.clear_actors(PELLET_GROUP)

        with open(PELLET_FILE, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            for r, row in enumerate(reader):
                
                x, y = int(row[0]) + FIELD_LEFT, int(row[1]) + FIELD_TOP
                type = row[2]
                position = Point(x, y)
                size = Point(PELLET_WIDTH, PELLET_HEIGHT)
                velocity = Point(0, 0)
                if type == "n":
                    image = Image(PELLET_IMAGE)
                    points = PELLET_POINTS
                elif type == "p":
                    image = Image(POWER_PELLET_IMAGE)
                    points = POWER_PELLET_POINTS

                body = Body(position, size, velocity)

                pellet = Pellet(body, image, points)
                cast.add_actor(PELLET_GROUP, pellet)

    def _add_cherry(self, cast):
        cast.clear_actors(CHERRY_GROUP)

        with open(CHERRY_FILE, 'r') as file:
            reader = csv.reader(file, skipinitialspace=True)
            for r, row in enumerate(reader):
                
                x, y = int(row[0]) + FIELD_LEFT, int(row[1]) + FIELD_TOP
                type = row[2]
                position = Point(x, y)
                size = Point(CHERRY_WIDTH, CHERRY_HEIGHT)
                velocity = Point(0, 0)
                if type == "c":
                    image = Image(CHERRY_IMAGE)
                    points = CHERRY_POINTS

                    body = Body(position, size, velocity)

                    cherry = Cherry(body, image, points)
                    cast.add_actor(CHERRY_GROUP, cherry)
    
    def _add_background(self, cast):
        cast.clear_actors(BG_GROUP)
        x = FIELD_LEFT
        y = FIELD_TOP

        position = Point(x, y)
        size = Point(BG_WIDTH, BG_HEIGHT)
        velocity = Point(0, 0)
        image = Image(BG_IMAGE)

        body = Body(position, size, velocity)

        bg = Wall(body, image, 0)
        cast.add_actor(BG_GROUP, bg)


    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_pacman(self, cast, pos):
        cast.clear_actors(PACMAN_GROUP)
        size = Point(PACMAN_WIDTH, PACMAN_HEIGHT)
        velocity = Point(0, 0)
        position = Point(pos.get_x() + FIELD_LEFT, pos.get_y() + FIELD_TOP)
        body = Body(position, size, velocity)
        animations = []
        animations.append(Animation(PACMAN_IMAGES["up"], PACMAN_RATE))
        animations.append(Animation(PACMAN_IMAGES["right"], PACMAN_RATE))
        animations.append(Animation(PACMAN_IMAGES["down"], PACMAN_RATE))
        animations.append(Animation(PACMAN_IMAGES["left"], PACMAN_RATE))
        pacman = Pacman(body, animations)
        cast.add_actor(PACMAN_GROUP, pacman)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_GHOST_ACTION)
        script.add_action(OUTPUT, self.DRAW_BG_ACTION)
        script.add_action(OUTPUT, self.DRAW_PELLETS_ACTION)
        script.add_action(OUTPUT, self.DRAW_PACMAN_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_GHOST_ACTION)
        script.add_action(UPDATE, self.MOVE_PACMAN_ACTION)
        script.add_action(UPDATE, self.COLLIDE_GHOST_ACTION)
        script.add_action(UPDATE, self.CONTROL_GHOST_ACTION)
        script.add_action(UPDATE, self.COLLIDE_GHOST_ACTION)
        script.add_action(UPDATE, self.COLLIDE_PELLETS_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)