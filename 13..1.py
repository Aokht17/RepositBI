class Virus:
    cellular = False

    def __init__(self, name, host, burst_size, particles, mortality):
        self.host = host
        self.name = name
        self.mortality = True
        self.burst_size = burst_size
        self.particles = particles

    def repl_cycle(self, animal):
        """
        shows the number of viral particles after infection of an appropriate host
        """
        if animal is self.host:
            self.particles += self.burst_size * 10000
        else:
            print('infection is abortive')
        return self.particles

    def mass_media(self):
        """
        keeps up to date with the latest news
        """
        if self.host is 'man' and self.mortality is True:
            print('WE ALL WILL DIE SOON FROM', self.name)
        else:
            print('SCIENTISTS HIDE THE TRUTH ABOUT', self.name)

    def how_many_vaccinated_to_prevent_epigemic(self, duration, population):
        """
        returns the percent of vaccinated people which is sufficient to ensure collective immunity
        :param duration: average disease duration (days)
        :param population: number of people (millions)
        """
        if self.host is 'man':
            gamma = (duration / 30)**(-1)
            sigma = gamma / 0.002
            p = 1 - sigma/population
            return int(p*100)


phage_mu = Virus('phage_mu','bacteria', 20000, 10, mortality=True)
coronavirus = Virus('coronavirus','man', 6400, 10, mortality=True)

phage_mu.mass_media()
print(coronavirus.how_many_vaccinated_to_prevent_epigemic(20, 7000))
print(coronavirus.repl_cycle('cat'))