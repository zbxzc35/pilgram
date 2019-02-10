# Copyright 2019 Akiomi Kamakura
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PIL import Image, ImageEnhance, ImageChops

from pilgram.sepia import sepia
from pilgram import util


def nashville(im):
    cb = im.convert('RGB')

    cs1 = util.fill(cb.size, [247, 176, 153])
    cs = ImageChops.darker(cb, cs1)
    cs = Image.blend(cb, cs, .56)

    cs2 = util.fill(cb.size, [0, 70, 150])
    cs_ = ImageChops.lighter(cs, cs2)
    cr = Image.blend(cs, cs_, .4)

    cr = sepia(cr, .2)
    cr = ImageEnhance.Contrast(cr).enhance(1.2)
    cr = ImageEnhance.Brightness(cr).enhance(1.05)
    cr = ImageEnhance.Color(cr).enhance(1.2)

    return cr.convert(im.mode)
