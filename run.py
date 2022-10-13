import alien_invasion
import settings

if __name__ == "__main__":
    settings = settings.PenalSettings()
    game = alien_invasion.MainGame(settings)
    game.start()