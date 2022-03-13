import math
import numpy as np
from collections import deque
from itertools import count, chain, cycle, combinations
import random
from tkinter import *
import colorsys
import time

SEG_LENGTH = 64
PLAY_LENGTH = 200
QUEUE_LENGTH = 512
NUM = 1250          # nr. of circles
R0, R1 = 30, 400    # radii, smallest & largest
LINE_WIDTH= 8

class Circle:

    def __init__(self, center, radius):
        self._center = list(center)
        self._radius = radius

    def __str__(self):
        return 'Radius: {}, center: {}'.format(self._radius, self._center)

    def get_radius(self):
        return self._radius

    def set_center(self, center):
        self._center = center

    def get_center(self):
        return self._center

    def point_to_theta(self, point):
        '''
        Input: a point on the circumferance.
        Return: theta in radians.
        N.B. arctan2 (2 arguments) can return the correct quadrant.
        '''
        p, center, r = point, self.get_center(), self.get_radius()
        x, y, ctr_x, ctr_y = p[0], p[1], center[0], center[1]
        theta = np.arctan2((y - ctr_y)/r, (x - ctr_x)/r)
        return theta


    def arcgen(self, start, stop):
        '''
        Input: start theta, stop theta in radians, the end pts of an arc.
        Return a generator of all the points in the arc.
        '''
        r, center = self.get_radius(), self.get_center()
        num = int(SEG_LENGTH * abs(stop - start)/ np.pi)

        lnsp = np.linspace(start, stop, num)
        xs = r * np.cos(lnsp) + center[0]
        ys = r * np.sin(lnsp) + center[1]

        return (point for point in zip(xs, ys))


    def line_from_center(self, angle):
        '''
        This was just a convenience fcn for testing durin dev.
        '''
        r, center = self.get_radius(), self.get_center()
        x, y = r * np.cos(angle) + center[0], r * np.sin(angle) + center[1]
        return (center[0], center[1], x, y)

    def dist(i, j):
        '''
        Return the distance between points i & j.
        '''
        x1, y1, x2, y2 = i[0], i[1], j[0], j[1]

        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def intersection(self, other):
        '''
        Input: two circles
        Output: the two points of itersection, z1 & z2, o.w. None
        In the calculation, a, h, & r0 are three sides of the right triangle.
        '''
        p0, p1 = self.get_center(), other.get_center()
        r0, r1 = self.get_radius(), other.get_radius()
        x0, y0, x1, y1 = p0[0], p0[1], p1[0], p1[1]
        dx, dy = x1 - x0, y1 - y0
        d = math.sqrt(dx ** 2 + dy **2)

        def are_exactly_two_pts_of_intersx(r1, r2, d):
            if d > r1+r2:
                return False
            elif d < abs(r1-r2):
                return False
            elif d == 0 and r1 == r2:
                return False
            else:
                return True

        if not are_exactly_two_pts_of_intersx(r0, r1, d):
            return None

        a = (r0 ** 2 - r1 ** 2 + d ** 2) / (2 * d)
        h = math.sqrt(r0 ** 2 - a ** 2)


        x2 = x0 + (a / d) * dx
        y2 = y0 + (a / d) * dy

        z1x = x2 + h * dy / d
        z2x = x2 - h * dy / d
        z1y = y2 - h * dx / d
        z2y = y2 + h * dx / d

        z1 = (int(z1x), int(z1y))
        z2 = (int(z2x), int(z2y))

        return z1, z2

class Player:
    def __init__(self):
        self._circlelist = self.make_circlelist()
        self._pairsdict = self.make_pairs_dict()
        self._playlist = self.make_playlist(length=PLAY_LENGTH)
        self._z_dict = self.make_z_dict()

    def __str__(self):
        'Circlelist: {}'.format(self._circlelist)

    def get_circlelist(self):
        return self._circlelist

    def get_z_dict(self):
        return self._z_dict

    def get_playlist(self):
        return self._playlist

    def make_circlelist(self):

        xs = np.random.randint(200, 2350, NUM)
        ys = np.random.randint(200, 1200, NUM)
        radii = np.random.randint(R0, R1, NUM)

        return [Circle((xs[idx], ys[idx]), radii[idx]) for idx in range(NUM)]

    def pairs(self):
        '''
        Return a list of 2-tuples.
        Each tuple consists of circlelist indices.
        Only pairs with intersections are returned.
        '''

        lst = self._circlelist
        indices = [idx for idx in range(len(lst))]
        combos = list(combinations(indices, 2))
        pairs = [(i, j) for (i, j) in combos if self.have_intersx(lst[i], lst[j])]

        return pairs

    def make_pairs_dict(self):
        '''
        Return pairs dict, 2 circles with intersection.
        keys: indices of the circles in circlelist.
        vals: list of circlelist indices that pair with the key.
        '''
        pairs0 = self.pairs()
        pairs = pairs0 + [tup[::-1] for tup in pairs0]
        pairs_dict = {}
        for tup in pairs:
            if tup[0] not in pairs_dict:
                pairs_dict[tup[0]] = [tup[1]]
            else:
                pairs_dict[tup[0]].append(tup[1])
        return pairs_dict

    def make_playlist(self, length):
        '''
        Input: length is no. of circles to traverse.
        Returns circlelist indices in the order they will play.
        '''
        c_list = self.get_circlelist()
        dict = self._pairsdict
        keylist = list(dict.keys())

        indices = []    # playlist indices
        indices.append(random.choice(keylist)) # choose a circle to start
        for idx in range(length - 1):
            next = random.choice(dict[indices[idx]])
            indices.append(next)

        return indices


    def arcgen_chain(self):
        '''
        Return a chained iterator of arc-generators.
        This is what is used by tk to produce lines.
        '''
        playlist = self.get_playlist() # circlelist indices
        circlelist = self.get_circlelist()
        z_dict = self.get_z_dict()

        arcgens = []
        start_theta = 0
        for idx in range(len(playlist) - 1):
            i, j = playlist[idx], playlist[idx + 1]
            z = random.choice(z_dict[(i, j)])               # endpoint of arc
            cir1, cir2 = circlelist[i], circlelist[j]
            stop_theta = cir1.point_to_theta(z)             ####
            if start_theta - stop_theta < 0.05:             # ~ pi / 90
                start_theta += random.choice([2 * np.pi, -2 * np.pi])
            # else:
            #     start_theta += random.choice([0, 0, 0, 0, 0, 0, 2 * np.pi]) # add or remove zeros
            gen = cir1.arcgen(start_theta, stop_theta)
            arcgens.append(gen)

            start_theta = cir2.point_to_theta(z) # start for next arc


        return chain(*arcgens)

    def make_z_dict(self):
        '''
        Return z_dict.
        keys: circlelist index pairs; pairs have intersections.
        values: [z1, z2] the points of intersection.
        '''

        z_dict = {}
        p_list = self.get_playlist()
        c_list = self.get_circlelist()

        pairs = self.pairs()

        for pair in pairs:
            idx, jdx = pair[0], pair[1]

            if (idx, jdx) not in z_dict:
                cir1, cir2 = c_list[idx], c_list[jdx]
                z1, z2 = cir1.intersection(cir2)
                z_dict[(idx, jdx)] = [z1, z2]
                z_dict[(jdx, idx)] = [z1, z2]

        return z_dict


    def have_intersx(self, circle1, circle2):
        '''
        Return True iff c1 & c2 have exactly two points of intersection.
        '''
        p0, p1 = circle1.get_center(), circle2.get_center()
        r0, r1 = circle1.get_radius(), circle2.get_radius()
        x0, y0, x1, y1 = p0[0], p0[1], p1[0], p1[1]
        dx, dy = x1 - x0, y1 - y0
        d = math.sqrt(dx ** 2 + dy **2)
        if d > r0 + r1:
            return False
        elif d < abs(r0 - r1):
            return False
        elif d == 0 and r0 == r1:
            return False
        else:
            return True



##################################################################################

# tk boilerplate & globals:
root = Tk()
geo_x, geo_y = root.winfo_screenwidth(), root.winfo_screenheight()
mid_x, mid_y = geo_x / 2, geo_y /2
root.geometry('%dx%d+%d+%d' % (500, 500, geo_x//2, geo_y//2))
c = Canvas(root, width=geo_x, height=geo_y, bg="black",
 bd=0, highlightthickness=0, relief="ridge")
c.pack(fill='both', expand=True)
root.wm_attributes('-fullscreen', 1)
hue0 = cycle(chain(np.linspace(0.1, 0.6, 300), np.linspace(0.99, 0.40, 400)))
hue1 = cycle(chain(np.linspace(0.5, 0.8, 300), np.linspace(0.7, 0.40, 300)))
hue2 = cycle(chain(np.linspace(0.01, 0.96, 1200), np.linspace(0.99, 0.05, 1200)))
hue3 = cycle(chain(np.linspace(0.8, 0.7, 100), np.linspace(0.99, 0.94, 50),
                   np.linspace(0.2, 0.25, 200), np.linspace(0.85, 0.8, 200),
                   np.linspace(0.4, 0.43, 100)))

##################################################################################

def get_color():

    h, s, l = next(hue2), 0.8, 0.45


    r, g, b = [int(256*i) for i in colorsys.hls_to_rgb(h,l,s)]
    return "#%02x%02x%02x" % (r, g, b)



def draw():
    p1 = Player()
    gen = p1.arcgen_chain()
    pt1 = next(gen)
    go = True
    dek = deque()
    while go == True:
        try:
            pt2 = next(gen)
            pt3 = next(gen)
            j = c.create_line(pt1[0], pt1[1], pt2[0], pt2[1], pt3[0], pt3[1], 
                              fill=get_color(), width=LINE_WIDTH)
            k = c.create_line(geo_x - pt1[0], geo_y - pt1[1], geo_x - pt2[0],
                              geo_y - pt2[1], geo_x - pt3[0], geo_y - pt3[1],
                              fill=get_color(), width=LINE_WIDTH)
            l = c.create_line(geo_x - pt1[0], pt1[1], geo_x - pt2[0], pt2[1],
                              geo_x - pt3[0], pt3[1],
                              fill=get_color(), width=LINE_WIDTH)
            m = c.create_line(pt1[0], geo_y - pt1[1], pt2[0], geo_y - pt2[1], pt3[0],
                              geo_y - pt3[1], fill=get_color(), width=LINE_WIDTH)
            pt1 = pt3

            dek.append(j); dek.append(k); dek.append(l); dek.append(m)
            root.update()
            if len(dek) > QUEUE_LENGTH:
                j = dek.popleft()
                k = dek.popleft()
                l = dek.popleft()
                m = dek.popleft()
                c.delete(j); c.delete(k); c.delete(l); c.delete(m)


        except StopIteration:
            go=False

def sleep():
    root.update()
    time.sleep(2)
    root.after(15000, sleep)

root.after(10000, sleep)
draw()
root.mainloop()
