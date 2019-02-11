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

from image4layer import Image4Layer
from PIL import Image, ImageEnhance

from pilgram import util


def clarendon(im):
    cb = im.convert('RGB')

    cs = util.fill(cb.size, [127, 187, 227])
    cs = Image4Layer.overlay(cb, cs)
    cr = Image.blend(cb, cs, .2)

    cr = ImageEnhance.Contrast(cr).enhance(1.2)
    cr = ImageEnhance.Color(cr).enhance(1.35)

    return cr.convert(im.mode)