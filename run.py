import alien_invasion
import settings

if __name__ == "__main__":
    settings = settings.Settings()
    game = alien_invasion.MainGame(settings)
    game.start()